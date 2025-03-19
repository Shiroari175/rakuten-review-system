$(document).ready(function() {
    $('#clearButton').click(function() {
        // テキスト入力フィールドをクリア
        $('#id-item_nm').val('');
        // ラジオボタンの選択をクリア
        $('input[type="radio"]').prop('checked', false);
    });
});

