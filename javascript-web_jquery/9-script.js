$(document).ready(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr',
    function (data, textStatus) {
      $('#hello').text(data.hello);
    });
});
