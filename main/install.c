#include <stdio.h>
#include <sys/stat.h>
#include <sys/types.h>

// Define directory names
#define  WORKING_PATH  "/home/juan/labnote"

#define  CONTENT_DIR   "content"
#define  DOCS_DIR      "documents"
#define  INVENTORY_DIR "inventory"

int main(void){
	FILE *fp;
	//fp = fopen("test.txt","w");
	//fprintf(fp, "Hello\n");
	//fclose(fp);
	mkdir(WORKING_PATH,0700);
	chdir(WORKING_PATH);
	mkdir(CONTENT_DIR,0700);
	mkdir(DOCS_DIR,0700);
	mkdir(INVENTORY_DIR,0700);
}
