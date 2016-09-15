#include <stdio.h>
#include <sys/stat.h>
#include <sys/types.h>

// Define directory names
#define  WORKING_PATH  "my_labnote_dir"
#define HOME "/home/lec"
#define  CONTENT_DIR   "content"
#define  DOCS_DIR      "documents"
#define  INVENTORY_DIR "inventory"
#define  GENERAL_DIR "general"

int main(void){
	FILE *fp;
	//fp = fopen("test.txt","w");
	//fprintf(fp, "Hello\n");
	//fclose(fp);
	chdir(HOME);
	mkdir(WORKING_PATH,0700);
	printf("Making the %s directory", WORKING_PATH);
	chdir(WORKING_PATH);
	mkdir(CONTENT_DIR,0700);
	mkdir(DOCS_DIR,0700);
	mkdir(INVENTORY_DIR,0700);
	mkdir(GENERAL_DIR,0700);
}
