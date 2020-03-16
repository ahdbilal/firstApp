package com.example.firstapp;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;

//import com.microsoft.appcenter.AppCenter;
//import com.microsoft.appcenter.distribute.Distribute;
//hahahah

public class MainActivity extends AppCompatActivity {


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Distribute.setEnabledForDebuggableBuild(true);
        // AppCenter.start(getApplication(), "cfa2fe7a-1303-4f8f-80c4-f8d69717968f", Distribute.class);
    }





}
