//  fetches from URL and displays the value of hello
$.ajax({
  url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
  method: 'GET',
  success: function (data) {
    $('#hello').text(data.hello);
  }
});
