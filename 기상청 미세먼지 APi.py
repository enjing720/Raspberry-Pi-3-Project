function callSKPlanetDust(lat, lon, appKey) {
	var request = new XMLHttpRequest();
	var url = 'http://apis.skplanetx.com/weather/dust';
 
	var queryParams = '?version=' + '1';
	queryParams += '&lat=' + lat;  // 위도
	queryParams += '&lon=' + lon;  // 경도
	queryParams += '&appKey=' + appKey;  // API 키 (SK플래닛 개발자센터에서 발급)
 
	request.open('GET', url + queryParams, true);
	request.onload = function () {
		if (request.status == 200) {
			var response = JSON.parse(request.responseText);
 
			console.log('response.result.message : %s', response.result.message);
			console.log('response.result.code : %s', response.result.code);
 
			var dust = response.weather.dust[0];
 
			console.log('dust.station.name : %s', dust.station.name);  // 근처 측정소명
			console.log('dust.station.id : %s', dust.station.id);
			console.log('dust.station.latitude : %s', dust.station.latitude);  // 측정소의 위도
			console.log('dust.station.longitude : %s', dust.station.longitude);  // 측정소의 경도
 
			console.log('dust.timeObservation : %s', dust.timeObservation);  // 미세먼지 측정시간
 
			console.log('dust.pm10.value : %s', dust.pm10.value);  // 미세먼지 수치
			console.log('dust.pm10.grade : %s', dust.pm10.grade);  // 등급(좋음, 보통... 등)
		} else {  // 에러 응답에 대한 대응
			console.log('request.status : %s', request.status);
			var response = JSON.parse(request.responseText);
 
			if(response.error) {
				console.log('response.category : %s', response.error.category);
				console.log('response.code : %s', response.error.code);
				console.log('response.id : %s', response.error.id);
				console.log('response.message : %s', response.error.message);
			}
		}
	};
	request.send(null);
}



response.result.message : 성공
response.result.code : 9200
dust.station.name : 수원
dust.station.id : 119
dust.station.latitude : 37.2723000000
dust.station.longitude : 126.9853000000
dust.timeObservation : 2016-05-20 17:00:00
dust.pm10.value : 90.75
dust.pm10.grade : 나쁨
 
실패 시(파라미터값을 누락) >
request.status : 400
response.category : system
response.code : 9401
response.id : 400
response.message : Request Parameter 검증에 실패하였습니다.
