$(document).ready(function () {
    $('#indexcontent').find('h2','h3').each(function() {
        var $item = $(this);
        var $id = $(this).attr('id');
        var li = $('<li/>');
        var a = $('<a/>', {text: $item.text(), href: '#' + $id, title: $item.text()});
        a.appendTo(li);
        $('#headings ul').append(li);
    });
});