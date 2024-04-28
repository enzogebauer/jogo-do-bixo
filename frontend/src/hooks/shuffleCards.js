//The shuffle function takes in an array (in this case the array of card objects) and returns a new shuffled array.
//It uses the Fisher-Yates algorithm for generating a random permutation of a finite sequence, where each permutation is
//equally likely.

export function shuffle(deckArray) {
	deckArray = deckArray.slice();

	for (let i = deckArray.length - 1; i > 0; i--) {
		const j = ~~(Math.random() * (i + 1));
		const x = deckArray[i];
		deckArray[i] = deckArray[j];
		deckArray[j] = x;
	}

	return deckArray;
}
