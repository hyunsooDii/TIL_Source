package com.example.recyclerview

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import kotlinx.android.synthetic.main.item_main.view.*

class MainAdapter : RecyclerView.Adapter<MainAdapter.MainViewHolder>() {

    var items: MutableList<MainData> = mutableListOf(
    MainData("Title1", "Content1"),
    MainData("Title2", "Content2"),
    MainData("Title3", "Content3"))

    // 3번째 호출출
   inner class MainViewHolder(itemView: View) :
        RecyclerView.ViewHolder(itemView) {
        val tvTitle = itemView.tv_main_title
        val tvContent = itemView.tv_main_content
    }

    // 2번째 호출
    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): MainViewHolder {
        val view = LayoutInflater.from(parent.context)
            .inflate(R.layout.item_main, parent, false)
        return MainViewHolder(view)
    }

    // 4번째 호출
    override fun onBindViewHolder(holder: MainViewHolder, position: Int) {
        items[position].let { item ->
            with(holder) {
                tvTitle.text = item.title
                tvContent.text = item.content
            }
        }
    }

    // 1번째 호출
    override fun getItemCount(): Int = items.size
}