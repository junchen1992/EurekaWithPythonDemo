package com.chenjun.eurekademo;

import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.web.bind.annotation.GetMapping;

public class DemoController {

    @FeignClient(value = "TETSEUREKACLIENT")
    public interface PythonFeignService {

        @GetMapping("test")
        String test();
    }
}
