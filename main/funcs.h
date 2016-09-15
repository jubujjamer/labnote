#include <stdio.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>
#include <time.h>
#include <locale.h>
#include <string.h>
#include "names.h"
/*
command-line tool to mangage the lab notebook.
usage
labnotebook -n creates a new folder in my_labnote_dir/content with today's name and opens an initialized .adoc file.
*/

void init_new_day(struct tm * today_date){
	FILE *fp;
	setlocale(LC_ALL, "");
	char buffer_fname[50], buffer_dayname[50],filename[50];
	strftime(buffer_fname, sizeof(filename), "%F", today_date);
	sprintf(filename,"%s.adoc",buffer_fname);
	strftime(buffer_dayname, sizeof(buffer_dayname), "%A %d de %B de %Y", today_date);
	printf("Creating %s file and folder.\n", filename);
	chdir(HOME);
	chdir(WORKING_PATH);
	chdir(CONTENT_DIR);
	mkdir(buffer_fname,0700);
	chdir(buffer_fname);
	fp = fopen(filename,"w");
	fprintf(fp,"= %s\nJuan Marco Bujjamer <jubujjamer@df.uba.ar>\n%s\n:toc:\n:icons: font\n",buffer_fname,buffer_dayname);
	fclose(fp);
	char command[50];
	sprintf(command,"atom %s.adoc",buffer_fname);
	system(command);
}
