#include "stdafx.h"
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <ctype.h>
#include <locale.h>		
#include <windows.h>

double RoundedToTwoDecimal(double value)
{
	return round(value * 100) / 100;
}

std::string TriangleTypeDefinition(double a, double b, double c)
{
	std::string typeTriangle = " ";
	if (a > 0 && b > 0 && c > 0)
	{
		if ((a + b < c) || (a + c < b) || (b + c < a))
		{
			typeTriangle = "Ошибка! Это не треугольник!";
		}
		else
		{
			std::vector<double> sides = { a, b, c };
			std::sort(sides.begin(), sides.end());

			double maxSide = sides[2];
			double averageSide = sides[1];
			double minSide = sides[0];

			if (maxSide != averageSide && minSide != averageSide)
			{
				typeTriangle = "Разносторонний ";
			}
			else if (maxSide != minSide)
			{
				typeTriangle = "Равнобедренный ";
			}
			else
			{
				typeTriangle = "Равносторонний ";
			}

			double sqrtSumMinSides = sqrt(averageSide*averageSide + minSide*minSide);
			if (RoundedToTwoDecimal(maxSide) == RoundedToTwoDecimal(sqrtSumMinSides))
			{
				typeTriangle += "Прямоугольный ";
			}
			else if (RoundedToTwoDecimal(maxSide) < RoundedToTwoDecimal(sqrtSumMinSides))
			{
				typeTriangle += "Острый ";
			}
			else if (RoundedToTwoDecimal(maxSide) > RoundedToTwoDecimal(sqrtSumMinSides))
			{
				typeTriangle += "Тупой ";
			}

			typeTriangle += "треугольник";
		}
	}
	else
	{
		typeTriangle = "Ошибка! Одна или более сторон не положительны";
	}
	return typeTriangle;
}

bool CheckStrToDouble(const std::string & numberStr)
{
	double number = atof(numberStr.c_str());
	std::stringstream ss;	  
	ss << number;							 
	return (numberStr == ss.str());
}

int main(int argc, char ** argv)
{
	SetConsoleOutputCP(1251);
	SetConsoleCP(1251);
	if (argc == 4)
	{
		if (CheckStrToDouble(argv[1]) && CheckStrToDouble(argv[2]) && CheckStrToDouble(argv[3]))
		{
			std::cout << TriangleTypeDefinition(atof(argv[1]), atof(argv[2]), atof(argv[3]));
		}
		else
		{
			std::cout << "Ошибка! Введено не число! Например: triangle.exe 3 4 5 (где 3 4 5 три стороны треугольника)";
		}
	}
	else
	{
		std::cout << "Ошибка! Неправильное количество параметров! Например: triangle.exe 3 4 5 (где 3 4 5 три стороны треугольника)" << std::endl;
	}
    return 0;
}