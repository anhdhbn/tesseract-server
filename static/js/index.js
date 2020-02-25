function readFile() {
  if (this.files && this.files[0]) {
    var FR= new FileReader();
    FR.addEventListener("load", function(e) {
      document.getElementById("imagestr").value = e.target.result.replace("data:image/png;base64,", "");
    }); 
    FR.readAsDataURL( this.files[0] );
  }
}

document.getElementById('fileToUpload').addEventListener('change', readFile)

const serialize_form = form => JSON.stringify(
  Array.from(new FormData(form).entries())
       .reduce((m, [ key, value ]) => Object.assign(m, { [key]: value }), {})
);

$('#form').on('submit', function(event) {
  event.preventDefault();
  const json = serialize_form(this);
  $.ajax({
    type: 'POST',
    url: 'api/ocr',
    dataType: 'json',
    data: json,
    contentType: 'application/json',
    dataType: 'json',
    success: function(data) {
      document.getElementById("result").value = data.result
    }
  });
});