// Toggles the class of the HTML tag HEADER to red (#FF0000)
// when the user clicks on the tag DIV#toggle_header
if (!$('HEADER').hasClass('red') && !$('HEADER').hasClass('green')) {
  $('HEADER').addClass('red');
  $('HEADER').removeClass('green');
}

$('DIV#toggle_header').click(() => {
  if ($('HEADER').hasClass('red')) {
    $('HEADER').addClass('green');
    $('HEADER').removeClass('red');
  } else {
    $('HEADER').addClass('red');
    $('HEADER').removeClass('green');
  }
});
