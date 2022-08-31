import py_eureka_client.eureka_client as eureka_client
import uvicorn
from fastapi import FastAPI

app = FastAPI(title='Eureka测试')


def set_eureka():
    eureka_server_list = "http://localhost:10234"  # Eureka注册中心地址,多个注册中心用，分割
    my_server_host = "127.0.0.1"  # 服务host
    my_server_port = 8881  # 服务端口
    eureka_client.init(eureka_server=eureka_server_list,
                       app_name="TetsEurekaClient",
                       instance_host=my_server_host,
                       instance_port=my_server_port
                       )


set_eureka()


@app.get('/test')
async def get_data():
    return "fastapi服务测试成功！"


@app.get('/testservice')
async def get_data():
    try:
        # 远程调用名为SENDER服务的send/1
        res = eureka_client.do_service(app_name="SENDER", service="/send/1", return_type="string")
        return "fastapi 调用远程服务结果：" + res
    except Exception as e:
        print(e)


if __name__ == '__main__':
    # reload 热加载，修改了自动重启
    uvicorn.run(app='TETSEUREKACLIENT:app', port=8881, reload=True)
