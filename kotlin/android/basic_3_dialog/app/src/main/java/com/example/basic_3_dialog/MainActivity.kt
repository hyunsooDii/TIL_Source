package com.example.basic_3_dialog

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.text.InputType
import android.widget.EditText
import android.widget.Toast
import androidx.appcompat.app.AlertDialog
import kotlinx.android.synthetic.main.activity_main.*
import org.jetbrains.anko.*

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        btnAlert.setOnClickListener {
            simpleAlertDialog()
            // ankoAlertDialog()
        }

        btnCustom.setOnClickListener {
            val dlg = MyDialog(this)
            dlg.setOnDismissListener {
                Toast.makeText(this, "${dlg.dayString}입니다.",
                    Toast.LENGTH_LONG).show()
                // 위 두줄 없이 아래처럼도 운용 가능
                // LongToast("${dlg.dayString}입니다.")
            }
            dlg.show()
        }
    }

    private fun ankoAlertDialog() {
        alert("타이틀입니다.", "메시지입니다.") {
            yesButton { toast("Oh...")}
            noButton {}
        }.show()
    }

    private fun simpleAlertDialog() {
        val builder = AlertDialog.Builder(this)  // context(컨택스트)

        builder.setTitle("타이틀입니다")

        val input = EditText(this)
        input.inputType = InputType.TYPE_CLASS_TEXT
        builder.setView(input)
        // builder.setIcon(R.mipmap.ic_launcher_round)

        builder.setMessage("메시지입니다")

        builder.setPositiveButton("OK", { dialog, which -> title = input.text.toString() })
        // 앱의 타이틀을 바꿔준다.

        builder.setNegativeButton("Cancel") {
                dialog, which -> dialog.cancel()
        } // 마지막 매개변수가 람다 함수면 괄호 바깥으로 빼는게 권장 사항

        // builder.show()

        builder.setCancelable(false)  // 뒤로가기 버튼을 터치해도 안닫힘

        val dialog = builder.create()
        dialog.setCanceledOnTouchOutside(false)  // 영역 밖에서 터치해도 사라지지 않음
        dialog.show()
    }
}