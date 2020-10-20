package com.example.basic_2_activitylife

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.view.ActionMode

class MainActivity : AppCompatActivity() {
    var nLineNumber = 0

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        Log.d("ALLTEST","${nLineNumber++} onCreate")
    }

    override fun onStart() {
        super.onStart()
        Log.d("ALLTEST","${nLineNumber++} onStart")
    }

    override fun onResume() {
        super.onResume()
        Log.d("ALLTEST","${nLineNumber++} onResume")
    }

    override fun onStop() {
        super.onStop()
        Log.d("ALLTEST","${nLineNumber++} onStop")
    }

    override fun onDestroy() {
        super.onDestroy()
        Log.d("ALLTEST","${nLineNumber++} onDestroy")
    }

}