$(document).ready(function() {
    $('#clearButton').click(function() {
        // テキスト入力フィールドをクリア
        //$('input[type="text"]').val('');
        $('#id-item_nm').val('');

        // ラジオボタンの選択をクリア
        $('input[type="radio"]').prop('checked', false);
//        $('#id-rating1').prop('checked', false);
//        $('#id-rating2').prop('checked', false);
//        $('#id-rating3').prop('checked', false);
//        $('#id-rating4').prop('checked', false);
//        $('#id-rating5').prop('checked', false);



    });
});

