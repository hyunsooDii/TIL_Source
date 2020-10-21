package com.example.stopwatch

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import android.widget.TextView
import kotlinx.android.synthetic.main.activity_main.*
import java.util.*
import kotlin.concurrent.timer

class MainActivity : AppCompatActivity() {
    private var time = 0
    private var isRunning = false
    private var timerTask: Timer? = null
    private var lap = 1

    private fun start() {
        fab.setImageResource(R.drawable.ic_baseline_pause_24)
        timerTask = timer(period = 10) {
            time++ // 타이머 작업
            val sec = time / 100
            val milli = time % 100
            runOnUiThread { // 람다 함수
                secTextView.text = "$sec" // UI 업데이트 작업
                milliTextView.text = "$milli"
            }
        }
    }
    private fun pause() {
        fab.setImageResource(R.drawable.ic_baseline_play_arrow_24)
        timerTask?.cancel() // if((timerTask != null) timerTask.cancel()
    }

    private fun reset() {
        timerTask?.cancel()
        // 모든 변수 초기화
        time = 0
        isRunning = false
        fab.setImageResource(R.drawable.ic_baseline_play_arrow_24)
        secTextView.text = "0"
        milliTextView.text = "00"
        // 모든 랩타임을 제거
        lapLayout.removeAllViews()
        lap = 1
    }

    private fun recordLapTime() {
        val lapTime = this.time
        val textView = TextView(this)
        textView.text = "$lap LAB : ${lapTime / 100}.${lapTime % 100}"
        // 맨 위에 랩타임 추가
        lapLayout.addView(textView, 0)
        lap++
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        fab.setOnClickListener {
            isRunning = !isRunning
            if (isRunning) { start() }
            else { pause() }
        }
        resetFab.setOnClickListener {
            reset()
        }
        lapButton.setOnClickListener {
            recordLapTime()
        }
    }
}