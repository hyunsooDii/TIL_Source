package com.example.mywebbrowser

import android.content.Intent
import android.net.Uri
import android.os.Bundle
import android.util.Log
import android.view.ContextMenu
import com.google.android.material.floatingactionbutton.FloatingActionButton
import com.google.android.material.snackbar.Snackbar
import androidx.appcompat.app.AppCompatActivity
import android.view.Menu
import android.view.MenuItem
import android.view.View
import android.view.inputmethod.EditorInfo
import android.webkit.WebViewClient
import kotlinx.android.synthetic.main.content_main.*
import org.jetbrains.anko.*
import kotlin.concurrent.timer

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        setSupportActionBar(findViewById(R.id.toolbar))

        // 컨텍스트 메뉴 등록
        registerForContextMenu(webView)

        // 웹뷰 기본 설정
        webView.apply { // this는 webView
            settings.javaScriptEnabled = true
            webViewClient = WebViewClient()
        }
        webView.loadUrl("http://www.google.com")

        urlEditText.setOnEditorActionListener { _, actionId, _ ->
            if (actionId == EditorInfo.IME_ACTION_SEARCH) {
                webView.loadUrl(urlEditText.text.toString())
                true // 람다 함수라 return값이 없다
            } else {
                false
            }
        }

    }

    var backCount = 0 // 뒤로가기 버튼 연속 클릭 횟수
    var counter = 0 // 타이머 함수 실행 횟수

    // 백 버튼 처리
    override fun onBackPressed() {
        if (webView.canGoBack()) {
            webView.goBack()
        } else {
            backCount++
            if (backCount == 1) {
                toast("종료하려면 한번 더 뒤로가기를 누르세요")
                timer(period = 3000) {
                    Log.e("--------------------", "---------------")
                    if (counter == 1) {
                        backCount = 0
                        counter = 0
                        cancel()
                    } else {
                        counter++
                    }
                }
            } else if (backCount == 2)
                super.onBackPressed()
        }
    }


    override fun onCreateOptionsMenu(menu: Menu): Boolean {
        // Inflate the menu; this adds items to the action bar if it is present.
        menuInflater.inflate(R.menu.menu_main, menu)
        return true
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        when (item?.itemId) {
            R.id.action_google, R.id.action_home -> {
                webView.loadUrl("http://www.google.com")
                return true
            }
            R.id.action_naver -> {
                webView.loadUrl("http://www.naver.com")
                return true
            }
            R.id.action_daum -> {
                webView.loadUrl("http://www.daum.net")
                return true
            }
            R.id.action_call -> {
                val intent = Intent(Intent.ACTION_DIAL)
                intent.data = Uri.parse("tel:031-123-4567")
                if (intent.resolveActivity(packageManager) != null) {
                    startActivity(intent)
                }
                return true
            }
            R.id.action_send_text -> {
                webView.url?.let { sendSMS("031-123-4567", it) }
                return true
            }
            R.id.action_email -> {
                webView.url?.let { email("test@example.com", it) }
                return true
            }
        }
        return super.onOptionsItemSelected(item)

    }
    // 컨텍스트 메뉴 작성
    override fun onCreateContextMenu(menu: ContextMenu?, v: View?,
                                     menuInfo: ContextMenu.ContextMenuInfo?) {
        super.onCreateContextMenu(menu, v, menuInfo)
        menuInflater.inflate(R.menu.menu_context, menu)
    }

    override fun onContextItemSelected(item: MenuItem): Boolean {
        when(item.itemId){
            R.id.action_share -> webView.url?.let { share(it) }
            R.id.action_browser -> webView.url?.let { share(it) }
        }
        return super.onContextItemSelected(item)
    }
}