package com.example.basic_1_textview

import android.graphics.Color
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.text.Html
import android.widget.Button
import android.widget.TextView

class MainActivity : AppCompatActivity() {

    var nCount : Int = 0

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        var txtNormal = findViewById<TextView>(R.id.textNormal)
        txtNormal.setOnClickListener {
            txtNormal.apply {
                setBackgroundColor(Color.RED)
                text = "Clicked!! ${nCount++}"
                setTextColor(Color.WHITE)
                setTextSize(28.0F)
            }
        }

        var txtHTML = findViewById<TextView>(R.id.textHTML)
        txtHTML.setOnClickListener {
            // setOnClickListener는 파라메터로 클릭한 Control인 View 객체를 넘겨준다.
            // 이름을 따로 정의하지 않으면, it으로 되어 있다.
            // it을 TextView로 캐스팅하고 사용할 수 있다.
            val htmlText = it as TextView
            htmlText.text = Html.fromHtml("<h1>Hi</h1>HTML<p style=\"color:red;\">Red</idv>")
            // fromHtml에 가운데줄은 권장하지 않는 메소드라는 뜻
        }
    }
}