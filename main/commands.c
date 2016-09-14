#include <stdio.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>


// Define directory names
int debug = 0;

int
main(int argc, char **argv)
{
	extern char *optarg;
	extern int optind;
	int c, err = 0;
	int mflag=0, pflag=0, fflag=0;
	char *sname = "default_sname", *fname;
	static char usage[] = "usage: %s [-dmp] -f fname [-s sname] name [name ...]\n";

	while ((c = getopt(argc, argv, "nf:nps:")) != -1)
		switch (c) {
		case 'd':
			debug = 1;
			break;
		case 'n':
			// Create newday
			mflag = 1;
			printf("Creating newdayfile!\n");
			return 0;
		case 'p':
			pflag = 1;
			break;
		case 'f':
			fflag = 1;
			fname = optarg;
			break;
		case 's':
			sname = optarg;
			break;
		case '?':
			err = 1;
			break;
		}
	if (fflag == 0) {	/* -f was mandatory */
		fprintf(stderr, "%s: missing -f option\n", argv[0]);
		fprintf(stderr, usage, argv[0]);
		return 1;
	} else if ((optind+1) > argc) {
		/* need at least one argument (change +1 to +2 for two, etc. as needeed) */

		printf("optind = %d, argc=%d\n", optind, argc);
		fprintf(stderr, "%s: missing name\n", argv[0]);
		fprintf(stderr, usage, argv[0]);
		return 1;
	} else if (err) {
		fprintf(stderr, usage, argv[0]);
		return 1;
	}
	/* see what we have */
	printf("debug = %d\n", debug);
	printf("pflag = %d\n", pflag);
	printf("mflag = %d\n", mflag);
	printf("fname = \"%s\"\n", fname);
	printf("sname = \"%s\"\n", sname);

	if (optind < argc)	/* these are the arguments after the command-line options */
		for (; optind < argc; optind++)
			printf("argument: \"%s\"\n", argv[optind]);
	else {
		printf("no arguments left to process\n");
	}
	return 0;
}
