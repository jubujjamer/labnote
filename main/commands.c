#include <stdio.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>


// Define directory names

int main(int argc, char *argv[]){
	int opt = 0;
	char *in_fname = NULL;
	char *out_fname = NULL;
	FILE *fp;

	while ((opt = getopt(argc, argv, "n:o:")) != -1) {
		switch(opt) {
			case 'n':
	    	printf("\nNo arguments on this");
	    		break;
	    		case 'o':
	    			out_fname = optarg;
	    			printf("\nOutput option value=%s", out_fname);
	    			break;
	    		case '?':
	    			/* Case when user enters the command as
	     			* $ ./cmd_exe -i
	     			*/
	    		if (optopt == 'o') {
	    			printf("\nMissing mandatory output option");
	  			}
					else if (optopt == 'n') {
	    			printf("\nCreating a new file");
						mkdir("day folder",0700);
						fp = fopen("day.adoc","w");
						fprintf(fp, "Hello\n");
						fclose(fp);
	  			}
					else {
	    			printf("\nInvalid option received");
	  			}
	  			break;
	 		}
		}
		printf("\n");
		return 0;
}
