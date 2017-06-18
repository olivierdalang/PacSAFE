# -*- coding: utf-8 -*-
"""
/***************************************************************************
 PacSafeDialog
                                 A QGIS plugin
 PacSAFE produces realistic natural hazard impact scenarios for better planning, preparedness and response activities for Pacific Countries
                             -------------------
        begin                : 2015-03-29
        git sha              : $Format:%H$
        copyright            : (C) 2015 by Secretariat of the Pacific Community
        email                : sachindras@spc.int
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from PyQt4.QtGui import *
from PyQt4 import QtGui, uic
from PyQt4.QtCore import pyqtSlot,SIGNAL,SLOT

#import resources
#import resources_rc


FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'PacSafe_dialog_base.ui'))


class PacSafeDialog(QtGui.QDialog, FORM_CLASS):
    
   
    
    
    def __init__(self, parent=None):
        """Constructor."""
        super(PacSafeDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        
        #QtGui.QMessageBox.about(self, "sdsadas", "dasdas")
       
        
        
      

    
