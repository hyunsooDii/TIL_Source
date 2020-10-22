package com.example.basic_3_dialog

import android.app.Dialog
import android.content.Context
import android.os.Bundle
import kotlinx.android.synthetic.main.dialog_my.*

class MyDialog(ctx : Context) : Dialog( ctx ) {
    open var dayString = ""
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.dialog_my)

        // 캘린터 Control의 일정이 바뀔 경우
        // 발생하는 이벤트핸들러 등록 및 구현
        calendarView.setOnDateChangeListener { view, year, month, dayOfMonth ->
            dayString = "${year}-${month + 1}-${dayOfMonth} " // 월이 0월부터 시작한다.
            // 월에 +1 해주자!
            txtSelectDate.text = dayString
        }

        btnOk.setOnClickListener{
            dismiss() // 다이얼로그 닫기
        }
        btnCancel.setOnClickListener {
            dayString = ""
            dismiss()
        }
    }
}