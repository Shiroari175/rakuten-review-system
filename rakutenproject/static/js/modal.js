$(document).ready(function() {

    // モーダルを開くボタンのクリックイベント
    $('#open-modal-btn').click(function () {
        console.log('')
        const recordId = $(this).data('record-id'); // data属性からIDを取得
        // Ajaxリクエストを送信
        $.ajax({
            url: `/modal-data/${recordId}/`, // Djangoのエンドポイント
            method: 'GET',
            dataType: 'json',
            success: function (data) {
        if (data.error) {
            $('#modal-content').text(`エラー: ${data.error}`);
        } else {
            // 取得したデータをモーダルに設定
//            $('#modal-content').html(`
//              <p>アイテム名: ${data.item_name}</p>
//              <p>レビュー: ${data.review}</p>
//            `);
        }
        // モーダルを表示
        $('#myModal').css('display', 'block');
    },
    error: function (xhr, status, error) {
            console.error('リクエストエラー:', error);
            $('#modal-content').text('データの取得に失敗しました。');
            $('#myModal').css('display', 'block');
        },
    });
});

// モーダルを閉じるボタンのクリックイベント
$('#close-modal-btn, #close-modal-btn-footer').click(function () {
      $('#myModal').css('display', 'none');
    });
});

//JS板
//document.getElementById('open-modal-btn').addEventListener('click', function () {
//    const modal = document.getElementById('myModal');
//    const modalContent = document.getElementById('modal-content');
//    const recordId = this.dataset.recordId; // ボタンにデータ属性としてIDを設定している場合
//
//    // Ajaxリクエスト
//    fetch(`/modal-data/${recordId}/`)
//        .then(response => response.json())
//        .then(data => {
//            if (data.error) {
//                modalContent.textContent = data.error;
//            } else {
//                modalContent.textContent = `アイテム: ${data.item_name}, レビュー: ${data.review}`;
//            }
//            // モーダルを表示
//            const bootstrapModal = new bootstrap.Modal(modal);
//            bootstrapModal.show();
//        })
//        .catch(error => {
//            console.error('エラー:', error);
//        });
//});


