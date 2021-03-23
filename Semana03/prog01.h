 #include <iostream>
 #include <cmath>
using namespace std;

struct z
{
  float R; // parte real
  float I; // parte imaginaria
  float raio; // raio
  float angulo; // angulo
};


float soma (float ra, float rb, float ia, float ib)
{
    float real = ra + rb;
    float imaginario = ia + ib;
    cout << "Resultado: " << real << " + j" << imaginario;
    return 0.0;
}

float subtrai (float ra, float rb, float ia, float ib)
{
    float real = ra - rb;
    float imaginario = ia - ib;
    cout << "Resultado: " << real << " + j" << imaginario;
    return 0.0;
}

float multiplica (float ra, float rb, float ia, float ib)
{
    float real = ra*rb - ia*ib;
    float imaginario = ra*ib + ia*rb;
    cout << "Resultado: " << real << " + j" << imaginario;
    return 0.0;
}

float divide (float ra, float rb, float ia, float ib)
{
    float real = (ra*rb + ia*ib)/(rb*rb + ib*ib);
    float imaginario = (rb*ia - ra*ib)/(rb*rb + ib*ib);
    cout << "Resultado: " << real << " + j" << imaginario;
    return 0.0;
}

float pol2ret (float raio, float angulo)
{
    float angRAD = angulo*3.14159/180;
    float real = raio * cos(angRAD);
    float imaginario = raio * sin(angRAD);
    cout << "Resultado: " << real << " + j" << imaginario;
    return 0.0;
}

float ret2pol (float real, float imaginario)
{
    float raio = sqrt(real*real + imaginario*imaginario);
    float angulo = atan(imaginario/real);
    cout << "Resultado: " << raio << " <" << angulo;
    return 0.0;
}