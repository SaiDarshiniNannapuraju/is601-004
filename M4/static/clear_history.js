function addToTextArea(char) {
  if(calcScreen.value.length < 5) {
      //here we are able to append text to the existing text and render
      calcScreen.value += char;
  }
}
