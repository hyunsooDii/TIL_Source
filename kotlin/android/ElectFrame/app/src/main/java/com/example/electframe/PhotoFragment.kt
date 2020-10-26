package com.example.electframe

import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import com.bumptech.glide.Glide
import kotlinx.android.synthetic.main.fragment_photo.*

private const val ARG_URI = "url"

class PhotoFragment : Fragment() {
    private var uri: String? = null

    // 데이터 초기화, View는 아직 없음
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        arguments?.let {
            uri = it.getString(ARG_URI)
        }
    }

    // View 생성
    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        return inflater.inflate(R.layout.fragment_photo, container, false)
    }

    // 프래그먼트 뷰 초기화
    override fun onViewCreated(view: View,
                               savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        // Glide로 이미지 로드하기
        Glide.with(this).load(uri).into(imageView)
    }

    companion object {
        // 외부에서 프래그먼트를 생성할 수 있도록 하는 factory 메소드 정의
        // 비슷한 예로 : Toast.makeText()
        @JvmStatic
        fun newInstance(uri: String) =
            PhotoFragment().apply {
                arguments = Bundle().apply {
                    putString(ARG_URI, uri)
                }
            }
    }
}