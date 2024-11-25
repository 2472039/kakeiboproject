// CSRFトークンを取得する関数
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

document.getElementById('logout-link').addEventListener('click', function (event) {
    event.preventDefault(); // デフォルトのリンク動作を無効化
    const csrftoken = getCookie('csrftoken'); // getCookie 関数を呼び出し

    fetch("{% url 'accounts:logout' %}", {
        method: "POST",
        headers: {
            "X-CSRFToken": csrftoken, // CSRFトークンをヘッダーに追加
            "Content-Type": "application/json",
        },
    }).then(response => {
        if (response.ok) {
            window.location.href = "{% url 'accounts:logout_success' %}"; // ログアウト完了ページへリダイレクト
        } else {
            alert("Logout failed!");
        }
    });
});
