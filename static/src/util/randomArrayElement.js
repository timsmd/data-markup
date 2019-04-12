export default function (inputArray) {
	let rand_index = Math.floor(Math.random() * inputArray.length);
	let element = inputArray[rand_index];
	element.index = rand_index;
	return element;
}