//$(document).ready(function () {
//    var form = $('#form_buying_product');

//    function cartUpdating(product_id, nmb) {
//        var data = {};
//        data.product_id = product_id;
//        data.nmb = nmb;
//        var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();
//        data.csrfmiddlewaretoken = csrf_token;
//
//
//        var url = form.attr("action");
//
//
//        $.ajax({
//            url: url,
//            type: 'POST',
//            data: data,
//            cache: true,
//            success: function (data) {
//                console.log("OK");
//                if (data.products_total_nmb || data.products_total_nmb == 0){
//                    $('#cart_total_nmb').text("(" + data.products_total_nmb + ")");
//                    $('.cart-items ul').html("");
//                    $.each(data.products, function (k, v) {
//                        $('.cart-items ul').append('<li>'+ v.name+', ' + v.nmb + 'шт. ' + 'по ' + v.price_per_item + 'грн  ' +
//                            '<a class="delete-item" href="" data-product_id="'+v.id+'">x</a>'+
//                            '</li>');
//                    });
//                }
//            },
//            error: function () {
//                console.log("error")
//            }
//
//        })
//
//
//    }
//
//    form.on('submit', function (e) {
//        e.preventDefault()
//        var nmb = $('#number').val();
//        var submit_btn = $('#submit_btn');
//        var product_id = submit_btn.data("product_id");
//        var product_name = submit_btn.data("name");
//        var product_price = submit_btn.data("price");
//
//
//        cartUpdating(product_id, nmb, is_delete = false)
//    });
//
//        $(document).on('click', '.delete-item', function (e) {
//        e.preventDefault();
//        product_id = $(this).data("product_id")
//        nmb = 0;
//        cartUpdating(product_id, nmb, is_delete = true)
//    });

//    $('.cart-btn').click(function (e) {
//        e.preventDefault();
//        $('.cart').fadeToggle('slow');
//    });

//});

//---------------Всплывающее окно------------------------

$(document).ready(function() { // зaпускaем скрипт пoсле зaгрузки всех элементoв
    /* зaсунем срaзу все элементы в переменные, чтoбы скрипту не прихoдилoсь их кaждый рaз искaть при кликaх */
    var overlay = $('#overlay'); // пoдлoжкa, дoлжнa быть oднa нa стрaнице
    var open_modal = $('.open_modal'); // все ссылки, кoтoрые будут oткрывaть oкнa
    var close = $('.modal_close, #overlay'); // все, чтo зaкрывaет мoдaльнoе oкнo, т.е. крестик и oверлэй-пoдлoжкa
    var modal = $('.modal_div'); // все скрытые мoдaльные oкнa

     open_modal.click( function(event){ // лoвим клик пo ссылке с клaссoм open_modal
         event.preventDefault(); // вырубaем стaндaртнoе пoведение
         var div = $(this).attr('href'); // вoзьмем стрoку с селектoрoм у кликнутoй ссылки
         overlay.fadeIn(200, //пoкaзывaем oверлэй
             function(){ // пoсле oкoнчaния пoкaзывaния oверлэя
                 $(div) // берем стрoку с селектoрoм и делaем из нее jquery oбъект
                     .css('display', 'block')
                     .animate({opacity: 1, top: '50%'}, 200); // плaвнo пoкaзывaем
         });
     });

     close.click( function(){ // лoвим клик пo крестику или oверлэю
            modal // все мoдaльные oкнa
             .animate({opacity: 0, top: '45%'}, 200, // плaвнo прячем
                 function(){ // пoсле этoгo
                     $(this).css('display', 'none');
                     overlay.fadeOut(400); // прячем пoдлoжку
                 }
             );
     });
});

//----------Конец всплывающего окна------------------

//-------------Анимация корзины------------------
    $('.window .close').click(function (e) {
e.preventDefault();
    $('#mask, .window').hide();
    });

    $('#mask').click(function () {
    $(this).hide();
    $('.window').hide();
    });

//-----------Конец анимации корзины----------------

$(document).on('submit', '#form-goods-adding', function(e){
    e.preventDefault();
    var form = $('#form-goods-adding');
    var url = form.attr("action");
    var data = $('#form-goods-adding').serialize();
//     data.csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        url: url,
        type: 'POST',
        data: data,
    })
    .done(function() {
        console.log("success");
        console.log(data);
    })
    .fail(function() {
        console.log("error");
    })
    .always(function() {

    });
    
})

