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

from OpenGL.GL import *
from PyQt4 import QtGui, QtOpenGL


class CheckVersion(QtOpenGL.QGLWidget):
    # create an openGL context for checking the version

    def __init__(self, parent=None):
        super(CheckVersion, self).__init__(parent)
        self.isSupported = 0

    def initializeGL(self):
        # Get the current version of openGL
        # Need to do it in initializeGL because a openGL context is needed

        versionString = glGetString(GL_VERSION)
        versionString = versionString.split('.')
        versionString = ''.join(versionString)
        try:
            versionInt = int(versionString)
            if(versionInt >= 310):
                self.isSupported = 1
            else:
                self.isSupported = 0
        except ValueError:
            self.isSupported = 0

        # Need version 3.1.0 or above
