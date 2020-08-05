// Thanks to Vishal on StackOverflow https://stackoverflow.com/questions/3443606/make-footer-stick-to-bottom-of-page-correctly
$(document).ready(function() {
    var docHeight = $(window).height();
    var footerHeight = $('.footer').height();
    var footerTop = $('.footer').position().top + footerHeight;
    if (footerTop < docHeight) {
        $('.footer').css('margin-top', (docHeight - footerTop) + 'px');
    }
});


// Thanks to Saran for a tutorial on how to do this. https://www.sanwebe.com/2013/03/addremove-input-fields-dynamically-with-jquery
$(document).ready(function() {
   var maxFields = 10;
   var parentDiv = $("#steps");
   var addButton = $("#addButton");
   var removeButton = $("#removeButton")

   var x = 1;
   $(addButton).click(function(event) {
       event.preventDefault();
       if(x < maxFields)
       {
           x++;
           $(parentDiv).append('<div class="input-group inputNum' + x + '"><div class="input-group-prepend">' +
                    '<span class="input-group-text">Step ' + x + '</span>' +
                '</div>' +
                '<input type="text" aria-label="First name" class="form-control" placeholder="What needs to be done in this step" name="step' + x + '">' +
                '<select name="numOfSuccesses' + x + '" class="form-control col-md-3" required>' +
                    '<option value="None">How Many Successes</option>' +
                    '<option value="1">1</option>' +
                    '<option value="2">2</option>' +
                    '<option value="3">3</option>' +
                    '<option value="4">4</option>' +
                    '<option value="5">5</option>' +
                    '<option value="6">6</option>' +
                    '<option value="7">7</option>' +
                    '<option value="8">8</option>' +
                    '<option value="9">9</option>' +
                    '<option value="10">10</option>' +
                    '<option value="11">11</option>' +
                    '<option value="12">12</option>' +
                    '<option value="13">13</option>' +
                    '<option value="14">14</option>' +
                    '<option value="15">15</option>' +
                    '<option value="16">16</option>' +
                    '<option value="17">17</option>' +
                    '<option value="18">18</option>' +
                    '<option value="19">19</option>' +
                    '<option value="20">20</option>' +
                    '<option value="21">21</option>' +
                '</select>' +
                '</div>');

                $("#stepsCount").val(x);
       }
   });

    $(removeButton).on("click", function(event) {
        event.preventDefault();
        if(x > 1)
        {
            $(".inputNum" + x).remove();
            x--;
            $("#stepsCount").val(x);
        }
    })
});


$(document).on('click', ".stepDoneBtn", function() {
    var td = $(this).parent();
    var current = Number(td.find(".currentComple").val());
    var goal = Number(td.find(".goalComple").text());
    var saveChangesBtn = td.closest("form").find(".saveChangesBtn");

    if (current < goal)
    {
        current++;
        td.find(".currentComple").val(current);
    }

    if (current == goal)
    {
        td.closest("tr").css("color", "#D3D3D3");
    }


    if (saveChangesBtn.css("visibility") === 'hidden')
    {
        saveChangesBtn.css("visibility", "visible");
    }

});


$(document).on('click', ".stepFailBtn", function() {

    var td = $(this).parent();
    var current = Number(td.find(".currentComple").val());
    var goal = Number(td.find(".goalComple").text());

    if (current <= goal && current > 0)
    {
      current--;
      td.find(".currentComple").val(current);
    }

    if (saveChangesBtn.css("visibility") === "hidden")
    {
      saveChangesBtn.css("visibility", "visible");
    }

    td.closest("tr").style.color = null;


});