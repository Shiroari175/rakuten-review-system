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

//                const results = response.data_item_nm;
//                const results_2 = response.data_evaluation;
                //let content = "";
                // レスポンスデータをループしてHTMLを生成
//                results.forEach(function(item) {
//                    content += `<p>${item}</p>`;
//                });
//                results_2.forEach(function(item) {
//                    content += `<p>${item}</p>`;
//                });

                // Base64エンコードされた画像を取得
                const chartData = response.chart;
                // モーダル内の画像を更新
                $("#chartImage").attr("src", "data:image/png;base64," + chartData);

                // レスポンスデータをモーダルに設定
//                $("#modalContent").html(response.data_item_nm);
//                $("#modalContent2").html(response.data_evaluation);
            },
            error: function() {
                // エラーハンドリング
                $("#modalContent").html("エラーが発生しました。");
            }
        });
    });


    // モーダルを開くボタンのクリックイベント
    $('#open-modal-btn-aaaaa').click(function () {
        // console.log('modal start!')
        const recordId = $(this).data('record-id'); // data属性からIDを取得
        // Ajaxリクエストを送信
        $.ajax({
            url: '/rak/modal_data/', // Djangoのエンドポイント
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
});

// モーダルを閉じるボタンのクリックイベント
//$('#close-modal-btn, #close-modal-btn-footer').click(function () {
//  $('#myModal').css('display', 'none');
//});

