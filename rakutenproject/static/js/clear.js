$(document).ready(function() {
    $('#clearButton').click(function() {
        // テキスト入力フィールドをクリア
        $('input[type="text"]').val('');
        // ラジオボタンの選択をクリア
        $('input[type="radio"]').prop('checked', false);
    });
});
