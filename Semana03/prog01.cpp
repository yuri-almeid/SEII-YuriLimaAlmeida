#include <iostream>
#include <prog01.h>
using namespace std;


int main() {

  z Za;
  z Zb;
  z Zc;

  // Za = 10 + j10
  Za.R = 10.0;
  Za.I = 10.0;

  // Zb = 20 + j20
  Zb.R = 20.0;
  Zb.I = 20.0;

  // Zc = 10 <30 graus
  Zc.raio = 10.0;
  Zc.angulo = 30.0;

  soma(Za.R, Zb.R, Za.I, Zb.I);
  subtrai(Za.R, Zb.R, Za.I, Zb.I);
  multiplica(Za.R, Zb.R, Za.I, Zb.I);
  divide(Za.R, Zb.R, Za.I, Zb.I);
  ret2pol(Za.R, Za.I);
  pol2ret(Zc.raio, Zc.angulo);
  return 0;
} 