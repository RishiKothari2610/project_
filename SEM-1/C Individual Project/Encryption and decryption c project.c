#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#include<string.h>
char* encrypt_algorithm(char *str, int key) 
{
    int i,len;
    char temp[40];
    char *cipher=malloc(40);
    len=strlen(str);
    for(i=0;i<=len;i++)
	{
        if(str[i]>='A' && str[i]<='Z')
		{
        	temp[i]=((str[i]-'A')+key)%26;
        	cipher[i]=temp[i]+'A';
        }
        else if(str[i]>='a' && str[i]<='z')
		{
            temp[i]=((str[i]-'a')+key)%26;
            cipher[i]=temp[i]+'a';
        }
        else
            cipher[i] = str[i];
    }
    cipher[len]='\0';
    return cipher;
}
char* decrypt_algorithm(char *str, int key) 
{
    int i,len;
    char temp[40];
    char *decrypt=malloc(40);
    len=strlen(str);
    for(i=0;i<len;i++) 
	{
        if(str[i]>='A' && str[i]<='Z') 
		{
            temp[i] = (str[i]-'A')-key;
            while(temp[i]<0) 
            temp[i]+=26;
            temp[i]=temp[i]%26;
            decrypt[i]=temp[i]+'A';
        } 
		else if(str[i] >= 'a' && str[i] <='z') 
		{
            temp[i]=(str[i]-'a')-key;
            while(temp[i]<0) 
            temp[i]+=26;
            temp[i]=temp[i]%26;
            decrypt[i]=temp[i]+'a';
        } 
		else 
        decrypt[i] = str[i];
    }
    decrypt[len]='\0';
    return decrypt;
}
void main() 
{
    int key;
    char *encryptedText,*decryptedText,text[40];
    printf("\nEnter the message to be encrypted: ");
    gets(text);
    printf("\nEnter the key: ");
    scanf("%d",&key);
    encryptedText=encrypt_algorithm(text,key);
    printf("\nEncrypted text is : %s",encryptedText);
    decryptedText=decrypt_algorithm(encryptedText,key);
    printf("\nDecrypted text is : %s",decryptedText);
}
