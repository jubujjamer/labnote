#include <stdio.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>


// Define directory names

int main(int argc, char *argv[]){
	int opt = 0;
	char *in_fname = NULL;
	char *out_fname = NULL;

	while ((opt = getopt(argc, argv, "newday:o:")) != -1) {
		switch(opt) {
	  	case 'i':
	    	in_fname = optarg;
	    	printf("\nInput option value=%s", in_fname);
	    	break;
	    case 'o':
	    	out_fname = optarg;
	    	printf("\nOutput option value=%s", out_fname);
	    	break;
	    case '?':
	    	/* Case when user enters the command as
	     	* $ ./cmd_exe -i
	     	*/
	    if (optopt == 'i') {
	    	printf("\nMissing mandatory input option");
	    	/* Case when user enters the command as
	     	* # ./cmd_exe -o
	     	*/
	  	}
			else if (optopt == 'o') {
	    	printf("\nMissing mandatory output option");
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
