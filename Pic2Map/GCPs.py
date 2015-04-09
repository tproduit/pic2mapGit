# -*- coding: utf-8 -*-
"""
/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4 import QtCore
from PyQt4 import QtGui

PCI, PCJ, LOCX, LOCY, LOCZ, CHECK, ERROR, PIXERROR = range(8)

MAGIC_NUMBER = 0x570C4
FILE_VERSION = 1


class GCP(object):

    def __init__(self, picture_i=0., picture_j=0., local_x=0., local_y=0., local_z=0., check=1, error=0, pixerror=0):
        print "GCP _init_"
        self.picture_i = picture_i
        self.picture_j = picture_j
        self.local_x = local_x
        self.local_y = local_y
        self.local_z = local_z
        self.check = check
        self.error = error
        self.pixerror = pixerror


class GCPTableModel(QtCore.QAbstractTableModel):

    def __init__(self, filename=""):
        super(GCPTableModel, self).__init__()
        self.filename = filename
        self.dirty = False
        self.GCPs = []
        self.pictures_i = set()
        self.pictures_j = set()
        self.locals_x = set()
        self.locals_y = set()
        self.locals_z = set()
        self.checks = set()
        self.errors = set()
        self.pixerrors = set()

    def flags(self, index):
        if not index.isValid():
            return QtCore.Qt.ItemIsEnabled
        return QtCore.Qt.ItemFlags(QAbstractTableModel.flags(self, index) |
                                   QtCore.Qt.ItemIsEditable)

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if not index.isValid() or \
           not (0 <= index.row() < len(self.GCPs)):
            return
        GCP = self.GCPs[index.row()]
        column = index.column()
        if role == QtCore.Qt.DisplayRole:
            if column == PCI:
                return GCP.picture_i
            elif column == PCJ:
                return GCP.picture_j
            elif column == LOCX:
                return GCP.local_x
            elif column == LOCY:
                return GCP.local_y
            elif column == LOCZ:
                return GCP.local_z
            elif column == CHECK:
                return GCP.check
            elif column == ERROR:
                return GCP.error
            elif column == PIXERROR:
                return GCP.pixerror
        elif role == QtCore.Qt.TextAlignmentRole:
            return int(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        elif role == QtCore.Qt.BackgroundColorRole:
            return QColor(210, 230, 230)
        return

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.TextAlignmentRole:
            if orientation == QtCore.Qt.Horizontal:
                return int(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
            return int(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        if role != QtCore.Qt.DisplayRole:
            return
        if orientation == QtCore.Qt.Horizontal:
            if section == PCI:
                return "Picture u"
            elif section == PCJ:
                return "Picture v"
            elif section == LOCX:
                return "World x"
            elif section == LOCY:
                return "World y"
            elif section == LOCZ:
                return "World z"
            elif section == CHECK:
                return "Use as GCP"
            elif section == ERROR:
                return "3D error [m]"
            elif section == PIXERROR:
                return "Pixel error"
        return int(section + 1)

    def rowCount(self, index=QtCore.QModelIndex()):
        return len(self.GCPs)

    def columnCount(self, index=QtCore.QModelIndex()):
        return 8

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if index.isValid() and 0 <= index.row() < len(self.GCPs):
            GCP = self.GCPs[index.row()]
            column = index.column()
            if type(value) == unicode:
                try:
                    value = float(value)
                except:
                    value = 0
            if column == PCI:
                GCP.picture_i = value
            elif column == PCJ:
                GCP.picture_j = value
            elif column == LOCX:
                GCP.local_x = value
            elif column == LOCY:
                GCP.local_y = value
            elif column == LOCZ:
                GCP.local_z = value
            elif column == CHECK:
                GCP.check = value
            elif column == ERROR:
                GCP.error = value
            elif column == PIXERROR:
                GCP.pixerror = value
            self.dirty = True
            self.emit(SIGNAL("dataChanged(QtCore.QModelIndex,QtCore.QModelIndex)"),
                      index, index)
            return True
        return False

    def insertRows(self, position, rows=1, index=QtCore.QModelIndex()):
        self.beginInsertRows(
            QtCore.QModelIndex(), position, position + rows - 1)
        for row in range(rows):
            self.GCPs.insert(position + row, GCP())
        self.endInsertRows()
        self.dirty = True
        return True

    def removeRows(self, position, rows=1, index=QtCore.QModelIndex()):
        self.beginRemoveRows(QtCore.QModelIndex(), position,
                             position + rows - 1)
        self.GCPs = self.GCPs[:position] + \
            self.GCPs[position + rows:]
        self.endRemoveRows()
        self.dirty = True
        return True

    def load(self, filename):
        exception = None
        fh = None
        try:
            if not filename:
                raise IOError, "no filename specified for loading"
            fh = QtCore.QFile(filename)
            if not fh.open(QtCore.QIODevice.ReadOnly):
                raise IOError, unicode(fh.errorString())
            stream = QtCore.QDataStream(fh)
            magic = stream.readInt32()
            if magic != MAGIC_NUMBER:
                raise IOError, "unrecognized file type"
            fileVersion = stream.readInt16()
            if fileVersion != FILE_VERSION:
                raise IOError, "unrecognized file type version"
            self.GCPs = []
            while not stream.atEnd():
                picture_i = stream.readQVariant()
                picture_j = stream.readQVariant()
                local_x = stream.readQVariant()
                local_y = stream.readQVariant()
                local_z = stream.readQVariant()
                self.GCPs.append(
                    GCP(picture_i, picture_j, local_x, local_y, local_z))
                self.pictures_i.add(picture_i)
                self.pictures_j.add(picture_j)
                self.locals_x.add(local_x)
                self.locals_y.add(local_y)
                self.locals_z.add(local_z)
            self.dirty = False
        except IOError, e:
            exception = e
        finally:
            if fh is not None:
                fh.close()
            if exception is not None:
                raise exception

    def save(self, filename):
        exception = None
        fh = None
        try:
            if not filename:
                raise IOError, "no filename specified for saving"
            fh = QFile(filename)
            if not fh.open(QIODevice.WriteOnly):
                raise IOError, unicode(fh.errorString())
            stream = QtCore.QDataStream(fh)
            stream.writeInt32(MAGIC_NUMBER)
            stream.writeInt16(FILE_VERSION)
            if hasattr(QtCore.QDataStream, 'Qt_4_8'):
                stream.setVersion(QDataStream.Qt_4_8)
            for GCP in self.GCPs:
                stream.writeQVariant(GCP.picture_i)
                stream.writeQVariant(GCP.picture_j)
                stream.writeQVariant(GCP.local_x)
                stream.writeQVariant(GCP.local_y)
                stream.writeQVariant(GCP.local_z)
            self.dirty = False
        except IOError, e:
            exception = e
        finally:
            if fh is not None:
                fh.close()
            if exception is not None:
                raise exception

    def checkValid(self, rowIndex):
        valid = 1
        for i in range(0, 8):
            index = self.index(rowIndex, i)
            dat = self.data(index)
            if not isinstance(dat, (int, long, float)):
                valid = 0
        return valid
