#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>
#include <iostream>

int main()
{
    char dersler[7] = {'Matematik','Turkce','Fizik','Kimya','Biyoloji','Tarih','Ingilizce'};
    int notlar[];
	float ortalamalar[];

    int ortalamaHesaplama(int[])
    {
    	for (int i = 0; i < 7; i++){
    		
    		printf(i" 1.Sinav:");
            scanf("%d", &notlar[i]);
            printf(i" 2.Sinav:");
            scanf("%d", &notlar[i+1]);
                 
            ort=(notlar[i]+notlar[i+1])/2 , &ortalamalar[i];
            sum += ortalamalar[i];
		}
		gort = sum / 7, &ortalamalar[i];
	}
	
	char degerlendirme(float[])
	{
		for (int i = 0; i < ortalamalar[];i++ )
		{
			if(ortalamalar[i] >= 85 ){
                 	SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),2);
                 	printf(i": %10.2f", ortalamalar[i]);
                 	printf("%18s\n","COK IYI!");
				 }
				 else if (ortalamalar[i] < 85 && ortalamalar[i] >= 70){
				    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),6);
				 	printf(i": %10.2f", ortalamalar[i]);
				 	printf("%32s\n","DAHA COK CALISMALISIN!");
				 }
				 else{
				    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),4);
				 	printf(i": %10.2f", ortalamalar[i]);
				 	printf("%20s\n","IYI DEGIL!");
				 }
		}
	}
	
	int ortalamaHesaplama(int notlar[]);
	
	printf("\n\n%s%20s%20s\n","Ders","Ortalama","Degerlendirme");
	
	char degerlendirme(float ortalamalar[]);
	
	
	
	
	
	/*
	             printf("Matematik 1.Sinav:");
                 scanf("%d", &m1);
                 printf("Matematik 2.Sinav:");
                 scanf("%d", &m2);

                 printf("Turkce 1.Sinav:");
                 scanf("%d", &t1);
                 printf("Turkce 2.Sinav:");
                 scanf("%d", &t2);

                 printf("Fizik 1.Sinav:");
                 scanf("%d", &f1);
                 printf("Fizik 2.Sinav:");
                 scanf("%d", &f2);

                 printf("Kimya 1.Sinav:");
                 scanf("%d", &k1);
                 printf("Kimya 2.Sinav:");
                 scanf("%d", &k2);

                 printf("Biyoloji 1.Sinav:");
                 scanf("%d", &b1);
                 printf("Biyoloji 2.Sinav:");
                 scanf("%d", &b2);

                 printf("Tarih 1.Sinav:");
                 scanf("%d", &th1);
                 printf("Tarih 2.Sinav:");
                 scanf("%d", &th2);

                 printf("Ingilizce 1.Sinav:");
                 scanf("%d", &i1);
                 printf("Ingilizce 2.Sinav:");
                 scanf("%d", &i2);

                 mort=(m1+m2)/2;
                 tort=(t1+t2)/2;
                 fort=(f1+f2)/2;
                 kort=(k1+k2)/2;
                 bort=(b1+b2)/2;
                 thort=(th1+th2)/2;
                 iort=(i1+i2)/2;
                 gort=(mort+tort+fort+kort+bort+thort+iort)/7;


                 printf("\n\n%s%20s%20s\n","Ders","Ortalama","Degerlendirme");



                 if(mort >= 85 ){
                 	SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),2);
                 	printf("Matematik: %10.2f", mort);
                 	printf("%18s\n","COK IYI!");
				 }
				 else if (mort < 85 && mort >= 70){
				    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),6);
				 	printf("Matematik: %10.2f", mort);
				 	printf("%32s\n","DAHA COK CALISMALISIN!");
				 }
				 else{
				    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),4);
				 	printf("Matematik: %10.2f", mort);
				 	printf("%20s\n","IYI DEGIL!");
				 }


                 if(tort >= 85 ){
                 	SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),2);
                 	printf("Turkce: %13.2f", tort);
                 	printf("%18s\n","COK IYI!");
				 }
				 else if (tort < 85 && tort >= 70){
				    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),6);
				 	printf("Turkce: %13.2f", tort);
				 	printf("%32s\n","DAHA COK CALISMALISIN!");
				 }
				 else{
				 	SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),4);
				 	printf("Turkce: %13.2f", tort);
				 	printf("%20s\n","IYI DEGIL!");
				 }


                 if(fort >= 85 ){
                 	SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),2);
                 	printf("Fizik: %14.2f", fort);
                 	printf("%18s\n","COK IYI!");
				 }
				 else if (fort < 85 && fort >= 70){
				    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),6);
				 	printf("Fikik: %14.2f", fort);
				 	printf("%32s\n","DAHA COK CALISMALISIN!");
				 }
				 else{
				 	SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),4);
				 	printf("Fikik: %14.2f", fort);
				 	printf("%20s\n","IYI DEGIL!");
				 }


				 if(kort >= 85 ){
                 	SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),2);
                 	printf("Kimya: %14.2f", kort);
                 	printf("%18s\n","COK IYI!");
				 }
				 else if (fort < 85 && fort >= 70){
				    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),6);
				 	printf("Kimya: %14.2f", kort);
				 	printf("%32s\n","DAHA COK CALISMALISIN!");
				 }
				 else{
				 	SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),4);
				 	printf("Kimya: %14.2f", kort);
				 	printf("%20s\n","IYI DEGIL!");
				 }


				 if(bort >= 85 ){
                 	SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),2);
                 	printf("Biyoloji: %11.2f", bort);
                 	printf("%18s\n","COK IYI!");
				 }
				 else if (bort < 85 && bort >= 70){
				    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),6);
				 	printf("Biyoloji: %11.2f", bort);
				 	printf("%32s\n","DAHA COK CALISMALISIN!");
				 }
				 else{
				 	SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),4);
				 	printf("Biyoloji: %11.2f", bort);
				 	printf("%20s\n","IYI DEGIL!");
				 }


				 if(thort >= 85 ){
                 	SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),2);
                 	printf("Tarih: %14.2f", thort);
                 	printf("%18s\n","COK IYI!");
				 }
				 else if (thort < 85 && thort >= 70){
				    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),6);
				 	printf("Tarih: %14.2f", thort);
				 	printf("%32s\n","DAHA COK CALISMALISIN!");
				 }
				 else{
				 	SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),4);
				 	printf("Tarih: %14.2f", thort);
				 	printf("%20s\n","IYI DEGIL!");
				 }


				 if(iort >= 85 ){
                 	SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),2);
                 	printf("Ingilizce: %10.2f", iort);
                 	printf("%18s\n","COK IYI!");
				 }
				 else if (iort < 85 && iort >= 70){
				    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),6);
				  	printf("Ingilizce: %10.2f", iort);
				  	printf("%32s\n","DAHA COK CALISMALISIN!");
				 }
				 else{
				 	SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),4);
				 	printf("Ingilizce: %10.2f", iort);
				 	printf("%20s\n","IYI DEGIL!");
				 }


				 if(gort >= 85 ){
                 	SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),2);
                 	printf("Genel: %14.2f", gort);
                 	printf("%18s\n","COK IYI!");
				 }
				 else if (gort < 85 && gort >= 70){
				    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),6);
				 	printf("Genel: %14.2f", gort);
				 	printf("%32s\n","DAHA COK CALISMALISIN!");
				 }
				 else{
				 	SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),4);
				 	printf("\nGenel: %14.2f", gort);
				 	printf("%20s\n","IYI DEGIL!");
				 }
	*/			 
    return 0;
}
