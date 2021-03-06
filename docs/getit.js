function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

function editNote(id) {
	var title = document.getElementsByName('title-' + id)[0].innerText
	var content = document.getElementsByName('content-' + id)[0].innerText

	document.getElementsByName('id-hidden')[0].value = id
	document.getElementsByName('titulo')[0].value = title
	document.getElementsByName('detalhes')[0].value = content
}

function deleteForm(id) {
	var buttonDelete = document.getElementsByName('deleteForm-' + id)[0]
	buttonDelete.submit()
}

document.addEventListener("DOMContentLoaded", function () {
  let textareas = document.getElementsByClassName("autoresize");
  for (let i = 0; i < textareas.length; i++) {
    let textarea = textareas[i];
    function autoResize() {
      this.style.height = "auto";
      this.style.height = this.scrollHeight + "px";
    }

    textarea.addEventListener("input", autoResize, false);
  }

  // Sorteia classes de cores aleatoriamente para os cards
  let cards = document.getElementsByClassName("card");
  for (let i = 0; i < cards.length; i++) {
    let card = cards[i];
    card.className += ` card-color-${getRandomInt(
      1,
      5
    )} card-rotation-${getRandomInt(1, 11)}`;
  }
});



