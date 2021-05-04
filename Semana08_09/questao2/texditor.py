from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import * 
from PyQt5.QtPrintSupport import * 
import os
import sys
  
class MainWindow(QMainWindow):
  

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
  
       
        self.setGeometry(100, 100, 600, 400)
        layout = QVBoxLayout()
        self.editor = QPlainTextEdit()
        fixedfont = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        fixedfont.setPointSize(12)
        self.editor.setFont(fixedfont)
  
        self.path = None
  
        layout.addWidget(self.editor)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
  

        self.status = QStatusBar()
        self.setStatusBar(self.status)
        file_toolbar = QToolBar("Arquivo")
        self.addToolBar(file_toolbar)
        file_menu = self.menuBar().addMenu("&Arquivo")
        
        open_file_action = QAction("Abrir Arquivo", self)
        open_file_action.setStatusTip("Abrir Arquivo")
        open_file_action.triggered.connect(self.file_open)
        file_menu.addAction(open_file_action)

        save_file_action = QAction("Salvar", self)
        save_file_action.setStatusTip("Salvar pagina atual")
        save_file_action.triggered.connect(self.file_save)
        file_menu.addAction(save_file_action)

        saveas_file_action = QAction("Salvar como", self)
        saveas_file_action.setStatusTip("Salvar em diretorio diferente")
        saveas_file_action.triggered.connect(self.file_saveas)
        file_menu.addAction(saveas_file_action)
  
        print_action = QAction("Imprimir", self)
        print_action.setStatusTip("Imprimir Pagina")
        print_action.triggered.connect(self.file_print)
        file_menu.addAction(print_action)
  
        edit_toolbar = QToolBar("Editar")
  
        self.addToolBar(edit_toolbar)
  
        edit_menu = self.menuBar().addMenu("&Editar")
  

        undo_action = QAction("voltar", self)
        undo_action.setStatusTip("Volta (crtl+z)")
        undo_action.triggered.connect(self.editor.undo)
        edit_menu.addAction(undo_action)
  
        redo_action = QAction("Avançar", self)
        redo_action.setStatusTip("Avançar (crtl+y)")
        redo_action.triggered.connect(self.editor.redo)
        edit_menu.addAction(redo_action)
  

        cut_action = QAction("Cortar", self)
        cut_action.setStatusTip("Cortar")
        cut_action.triggered.connect(self.editor.cut)
        edit_menu.addAction(cut_action)
  

        copy_action = QAction("Copiar", self)
        copy_action.setStatusTip("Copiar")
        copy_action.triggered.connect(self.editor.copy)
        edit_menu.addAction(copy_action)
  
        paste_action = QAction("Colar", self)
        paste_action.triggered.connect(self.editor.paste)
        edit_menu.addAction(paste_action)
        
        select_action = QAction("Selecionar tudo", self)
        select_action.setStatusTip("Selecionar todo o texto")
        select_action.triggered.connect(self.editor.selectAll)
        edit_menu.addAction(select_action)
  
  

        wrap_action = QAction("Quebrar linha automatico", self)
        wrap_action.setStatusTip("Quebrar linha automatico")
        wrap_action.setCheckable(True)
        wrap_action.setChecked(True)
        wrap_action.triggered.connect(self.edit_toggle_wrap)
        edit_menu.addAction(wrap_action)
  
    
        self.update_title()
        self.show()
  
    
    def dialog_critical(self, s):
  

        dlg = QMessageBox(self)
        dlg.setText(s)
        dlg.setIcon(QMessageBox.Critical)
        dlg.show()
  

    def file_open(self):
  
        path, _ = QFileDialog.getOpenFileName(self, "Carregar arquivo", "", 
                             "Documento de texto (*.txt);All files (*.*)")

        if path:
            try:
                with open(path, 'rU') as f:
                    text = f.read()
  
           
            except Exception as e:
                self.dialog_critical(str(e))
            else:
                self.path = path
                self.editor.setPlainText(text)
                self.update_title()
  

    def file_save(self):
  
       
        if self.path is None:
            return self.file_saveas()
  
        self._save_to_path(self.path)
  

    def file_saveas(self):
  

        path, _ = QFileDialog.getSaveFileName(self, "Salvar Arquivo", "", 
                             "Documento de texto (*.txt);All files (*.*)")
  

        if not path:
            return
  
        self._save_to_path(path)
  

    def _save_to_path(self, path):
  

        text = self.editor.toPlainText()
        try:
  
            with open(path, 'w') as f:
                f.write(text)
  

        except Exception as e:

            self.dialog_critical(str(e))
  

        else:

            self.path = path
            self.update_title()
  

    def file_print(self):
  
        dlg = QPrintDialog()
        if dlg.exec_():
            self.editor.print_(dlg.printer())
  

    def update_title(self):
        self.setWindowTitle("%s - Texditor" %(os.path.basename(self.path) 
                                                  if self.path else "Sem título"))
  

    def edit_toggle_wrap(self):
        self.editor.setLineWrapMode(1 if self.editor.lineWrapMode() == 0 else 0 )
  
  

if __name__ == '__main__':
  
    app = QApplication(sys.argv)
    app.setApplicationName("Texditor")
    window = MainWindow()
    app.exec_()