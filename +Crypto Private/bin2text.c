#include <Windows.h>

void base58_encode (const char *in, char *out) {
	
	
}


void base58check_encode (const char *in, char *out, UINT8 version) {
	
}


/*

Version bytes

Decimal version		Leading symbol	Use
0					1 				Bitcoin pubkey hash (p2pkh)
5					3				Bitcoin script hash
21					4				Bitcoin (compact) public key (proposed)
52					M or N			Namecoin pubkey hash
128					5				Private key
111					m or n			Bitcoin testnet pubkey hash
196					2				Bitcoin testnet script hash 
*/

