$(document).ready(function() {

    $("#fetchData").on("click", function() {
        console.log('modal start!')

        // 選択された値を取得
        const selectedValue = $("#id-item_nm").val();

        // DjangoのViewにAjaxリクエストを送信
        $.ajax({
            url: "/rak/fetch-data/", // Djangoで定義するURLパス
            method: "POST",
            data: {
                value: selectedValue,
                csrfmiddlewaretoken: "{{ csrf_token }}" // CSRFトークンを追加
            },
            success: function(response) {

                // Base64エンコードされた画像を取得
                const chartData = response.chart;
                // モーダル内の画像を更新
                $("#chartImage").attr("src", "data:image/png;base64," + chartData);

                // レスポンスデータをモーダルに設定
//                $("#modalContent").html(response.data_item_nm);
            },
            error: function() {
                // エラーハンドリング
                $("#modalContent").html("エラーが発生しました。");
            }
        });
    });


});

// モーダルを閉じるボタンのクリックイベント
//$('#close-modal-btn, #close-modal-btn-footer').click(function () {
//  $('#myModal').css('display', 'none');
//});

