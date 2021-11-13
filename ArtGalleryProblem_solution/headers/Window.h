

#ifndef _WINDOW_H
#define _WINDOW_H

#include <QtGui>
#include "GLWidget.h"

class Window : public QMainWindow
{

public:
   Window(QWidget *parent = NULL);
   ~Window() {}
	
private:
   QWidget *centralWidget;
   GLWidget *glWidget;
   QHBoxLayout *mainLayout;
   QVBoxLayout *controlLayout;

   QPushButton *clearPolyButton;
   QPushButton *toggleTriangulateButton;
   QPushButton *toggleColorButton;
};

#endif /* _WINDOW_H */
