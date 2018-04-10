var fileList = [],
    arrFilterByName = [],
    uniqFileList = [];

function createFileList(file) {
    fileList.push(file);
}

//-------------------POST---------------------//
$(document).on('submit', '#form-goods-adding', function (e) {
    e.preventDefault();


    var formData = new FormData($('#form-goods-adding')[0]);
    var category = $("#category").val();
    formData.append("category", category);
    var currency = $("#currency").val();
    formData.append("currency", currency);
    var quantity = $("#quantity").val();
    formData.append("quantity", quantity);
    formData.delete("product_image");

    for (var x = 0; x < uniqFileList.length; x++) {
        formData.append("product_image", uniqFileList[x])
    }

    var url = $('#form-goods-adding').attr("action");

    $.ajax({
        url: url,
        data: formData,
        type: 'POST',
        xhr: function () {
            var xhr = new window.XMLHttpRequest();
            var progressBar = $('#progress-bar'),
                progressBg = progressBar.find('.progress-bg'),
                progressVal = progressBar.find('.progress-val');

            // Upload progress
            xhr.upload.addEventListener("progress", function (evt) {
                    if (evt.lengthComputable) {
                        var percentComplete = evt.loaded / evt.total;
                        percentComplete = (percentComplete * 100).toFixed();

                        progressBg.css('width', percentComplete + '%');
                        progressVal.text(percentComplete + '%');

                    }
                },
                false);
            return xhr;
        },

        contentType: false,
        processData: false

    })
        .done(function () {
            console.log("success");
            $('#form-goods-adding')[0].reset();
            $('#list').html("");
            $('#uploadImagesList').html("");
            fileList = [];
            arrFilterByName = [];
            uniqFileList = [];

        })
        .fail(function () {
            console.log("error");
            console.log(formData);
        })
        .always(function () {
        });
});

jQuery(document).ready(function ($) {

    var maxFileSize = 2 * 1024 * 1024; // (байт) Максимальный размер файла (2мб)
    var imagesList = $('#uploadImagesList');
    var itemPreviewTemplate = imagesList.find('.item.template').clone();
    itemPreviewTemplate.removeClass('template');
    imagesList.find('.item.template').remove();

    $('#inputGroupFile').on('change', function () {
        var files = this.files;

        for (var i = 0; i < files.length; i++) {
            var file = files[i];

            if (!file.type.match(/image\/(jpeg|jpg|png|gif)/)) {
                alert('Фотография должна быть в формате jpg, png или gif');
                continue;
            }

            if (file.size > maxFileSize) {
                alert('Размер фотографии не должен превышать 2 Мб');
                continue;
            }

            createFileList(file);
        }


        fileList.filter(function (file) {
            if (arrFilterByName.indexOf(file['name']) === -1) {
                arrFilterByName.push(file['name']);
                uniqFileList.push(file);
                return true
            }
            else {
                return false
            }
        });

        imagesList.html("");

        for (var k = 0; k < uniqFileList.length; k++) {
            preview(uniqFileList[k]);
        }


    });

    // Создание превью
    function preview(file) {
        var reader = new FileReader();
        reader.addEventListener('load', function (event) {
            var itemPreview = itemPreviewTemplate.clone();
            itemPreview.find('.img-wrap img').attr('src', event.target.result).attr('title', file.name);
            imagesList.append(itemPreview);
        });
        reader.readAsDataURL(file);
    }

    // Удаление фотографий
    imagesList.on('click', '.close', function () {
        var item = $(this).closest('.item'),
            id = item.data('id');

        item.remove();
        var index = arrFilterByName.indexOf(id);
        fileList.splice(index, 1);
        uniqFileList.splice(index, 1);
        arrFilterByName.splice(index, 1);

    });
});


$(document).on('submit', '#form-category-adding', function (e) {
    e.preventDefault();
    var form = $('#form-category-adding');
    var url = form.attr("action");
    var data = $('#form-category-adding').serialize();

    $.ajax({
        url: url,
        type: 'POST',
        data: data
    })
        .done(function () {
            console.log("success");
            $('#form-category-adding')[0].reset();
        })
        .fail(function () {
            console.log("error");
        })
        .always(function () {

        });

});

//-------------------END POST---------------------//

//
// //---------------Всплывающее окно------------------------//
//
$(document).ready(function () { // зaпускaем скрипт пoсле зaгрузки всех элементoв
    /* зaсунем срaзу все элементы в переменные, чтoбы скрипту не прихoдилoсь их кaждый рaз искaть при кликaх */
    var overlay = $('#overlay'); // пoдлoжкa, дoлжнa быть oднa нa стрaнице
    var open_modal = $('.open_modal'); // все ссылки, кoтoрые будут oткрывaть oкнa
    var close = $('.modal_close, #overlay'); // все, чтo зaкрывaет мoдaльнoе oкнo, т.е. крестик и oверлэй-пoдлoжкa
    var modal = $('.modal_div'); // все скрытые мoдaльные oкнa

    open_modal.click(function (event) { // лoвим клик пo ссылке с клaссoм open_modal
        event.preventDefault(); // вырубaем стaндaртнoе пoведение
        var div = $(this).attr('href'); // вoзьмем стрoку с селектoрoм у кликнутoй ссылки
        overlay.fadeIn(200, //пoкaзывaем oверлэй
            function () { // пoсле oкoнчaния пoкaзывaния oверлэя
                $(div) // берем стрoку с селектoрoм и делaем из нее jquery oбъект
                    .css('display', 'block')
                    .animate({opacity: 1, top: '50%'}, 200); // плaвнo пoкaзывaем
            });
    });

    close.click(function () { // лoвим клик пo крестику или oверлэю
        modal // все мoдaльные oкнa
            .animate({opacity: 0, top: '45%'}, 200, // плaвнo прячем
                function () { // пoсле этoгo
                    $(this).css('display', 'none');
                    overlay.fadeOut(400); // прячем пoдлoжку
                }
            );
    });
});

//----------Конец всплывающего окна------------------//

//-------------Анимация корзины------------------//
$('.window .close').click(function (e) {
    e.preventDefault();
    $('#mask, .window').hide();
});

$('#mask').click(function () {
    $(this).hide();
    $('.window').hide();
});

//-----------Конец анимации корзины----------------//

//--------------DROPDOWN MENU--------------------//

$(function () {
    $("#category_drop a").click(function () {
        $("#category:first-child").text($(this).text());
        $("#category:first-child").val($(this).text());
    });
});

$(function () {
    $("#currensy_drop a").click(function () {
        $("#currency:first-child").text($(this).text());
        $("#currency:first-child").val($(this).text());
    });
});

$(function () {
    $("#quantity_drop a").click(function () {
        $("#quantity:first-child").text($(this).text());
        $("#quantity:first-child").val($(this).text());
    });
});


// // $(document).ready(function () {
// //    var form = $('#form_buying_product');
// //
// //    function cartUpdating(product_id, nmb) {
// //        var data = {};
// //        data.product_id = product_id;
// //        data.nmb = nmb;
// //        var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();
// //        data.csrfmiddlewaretoken = csrf_token;
// //
// //
// //        var url = form.attr("action");
// //
// // //
// //        $.ajax({
// //            url: url,
// //            type: 'POST',
// //            data: data,
// //            cache: true,
// //            success: function (data) {
// //                console.log("OK");
// //                if (data.products_total_nmb || data.products_total_nmb == 0){
// //                    $('#cart_total_nmb').text("(" + data.products_total_nmb + ")");
// //                    $('.cart-items ul').html("");
// //                    $.each(data.products, function (k, v) {
// //                        $('.cart-items ul').append('<li>'+ v.name+', ' + v.nmb + 'шт. ' + 'по ' + v.price_per_item + 'грн  ' +
// //                            '<a class="delete-item" href="" data-product_id="'+v.id+'">x</a>'+
// //                            '</li>');
// //                    });
// //                }
// //            },
// //            error: function () {
// //                console.log("error")
// //            }
// //
// //        })
// //
// //
// //    }
// //
// //    form.on('submit', function (e) {
// //        e.preventDefault()
// //        var nmb = $('#number').val();
// //        var submit_btn = $('#submit_btn');
// //        var product_id = submit_btn.data("product_id");
// //        var product_name = submit_btn.data("name");
// //        var product_price = submit_btn.data("price");
// //
// //
// //        cartUpdating(product_id, nmb, is_delete = false)
// //    });
// //
// //        $(document).on('click', '.delete-item', function (e) {
// //        e.preventDefault();
// //        product_id = $(this).data("product_id")
// //        nmb = 0;
// //        cartUpdating(product_id, nmb, is_delete = true)
// //    });
//
// //    $('.cart-btn').click(function (e) {
// //        e.preventDefault();
// //        $('.cart').fadeToggle('slow');
// //    });
//
// //});