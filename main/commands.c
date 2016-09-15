/*******************************************************************************
Author: Juan Bujjamer
File: commands.c

command-line tool to mangage the lab notebook.
usage
keywords: today is today's date
-n adds new day.
-o datefile opens html file from the specified date.
-l lists wich files are included in the day's folder

*******************************************************************************/
#include <stdio.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>
#include <time.h>
#include "names.h"
#include "funcs.h"


int main(int argc, char **argv){
	extern char *optarg;
	extern int optind;
	int c, err = 0;
	int nflag=0, pflag=0, fflag=0;
	char *sname = "default_sname", *fname, *date_fname="default_fname";
	static char usage[] = "usage: %s [-dmp] -f fname [-s sname] name [name ...]\n";
	/*Dates information and formatting*/
	time_t t = time(NULL);
  	struct tm * today_date = localtime(&t);

	while ((c = getopt(argc, argv, "nf:o:s")) != -1)
		switch (c) {
		case 'n':
			// Create newday
			init_new_day(today_date);
			nflag = 1;
			return 0;
		case 'o':
			pflag = 1;
			date_fname = optarg;
			break;
		case 'f':
			fflag = 1;
			//fname = optarg;
			break;
		case 's':
			sname = optarg;
			break;
		case '?':
			err = 1;
			break;
		}
	if(pflag){
		open_day(date_fname);
		return 0;
	}
	if ((optind+1) > argc) {
		/* need at least one argument (change +1 to +2 for two, etc. as needeed) */
		printf("optind = %d, argc=%d\n", optind, argc);
		fprintf(stderr, "%s: missing name\n", argv[0]);
		fprintf(stderr, usage, argv[0]);
		return 1;
	} else if (err) {
		fprintf(stderr, usage, argv[0]);
		return 1;
	}
	if (optind < argc)	/* these are the arguments after the command-line options */
		for (; optind < argc; optind++)
			printf("argument: \"%s\"\n", argv[optind]);
	else {
		printf("no arguments left to process\n");
	}
	return 0;
}
