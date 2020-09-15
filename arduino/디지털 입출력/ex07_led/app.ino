#include <TrafficLight.h>

TrafficLight lights(12,13,7);

void setup()
{

}

// 2초간 직진 신호
// 2초간 직진, 좌회전 동시 신호
// 2초간 직진 및 좌회전 블링크
// 2초간 정지 신호
void loop()
{
    lights.run();
}
