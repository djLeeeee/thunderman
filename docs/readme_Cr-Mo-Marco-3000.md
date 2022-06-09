![Animation](readme_Cr-Mo-Marco-3000.assets/Animation.gif)



<center>
  <h1>
    THUNDERMAN
  </h1>
</center>
<center>
  <strong>
    SSAFY 7기 서울 3반 공식 번개 서비스
  </strong>
</center>

<center><stong><a href='https://thunderman.herokuapp.com/' style='text-decoration: none; color: #2159B0;'>페이지 방문하기</a></strong></center>

<div style='display:flex; justify-content: center;'>
        <img alt="Python" src ="https://img.shields.io/badge/Python-FFE15F.svg?&style=for-the-badge&logo=Python&logoColor=3776AB"/>
    <img alt="Django" src ="https://img.shields.io/badge/Django-092E20.svg?&style=for-the-badge&logo=Django&logoColor=white"/>
    <img alt="Heroku" src ="https://img.shields.io/badge/Heroku-430098.svg?&style=for-the-badge&logo=Heroku&logoColor=white"/>
</div>


---

<p style='display: flex; justify-content: center;'>
  <div style='display: flex; justify-content: center;'>
     <h3>
       Contents  
     </h3> 
  </div>
  <div style='display: flex; justify-content: center;'>
  	<strong>
	  <a style="text-decoration: none;" href="#인트로">인트로</a> | 
	  <a style="text-decoration: none;" href="#메인 서비스 소개">메인 서비스 소개</a> |
      <a style="text-decoration: none;" href="#부가 기능 소개">부가 기능 소개</a>
    </strong>
  </div>
</p>




## 인트로

### 서비스 개발 동기

* 2022년 상반기 코로나로 인한 비대면 수업의 지속으로 반 구성원 사이의 친밀감 형성이 어려웠습니다.
* 전체 단톡방에서 모임에 대한 공지를 했더라도 그 이후 다른 대화들이 오갈 경우 모임에 대한 글을 재확인하기 어려운 상황이 있었습니다.

* 프로젝트 주제 선정 당시 정부 정책에 의해 모임 인원에 제한이 남아 있었기 때문에, 단톡방에서 다소 늦게 공지를 확인 한 경우, 남은 자리가 있는지에 대한 정보, 약속 참석 여부등을 모임 주최자에게 1:1로 따로 물어야 하는 불편함이 있었습니다.

* 위에서 언급한 여러 불편함을 해결하기 위하여 약속에 대한 정보만 쉽게 확인 할 수 있고, 참석 인원 정보를 바로바로 알 수 있는 모임 사이트를 만들기로 결정했습니다.



## Service Description



### 메인 서비스 소개



#### 메인 페이지

---

<img src="readme_Cr-Mo-Marco-3000.assets/image-20220609193301928.png" alt="image-20220609193301928" style="zoom:50%;" />

- 30 일 이내에 약속이 있다면, 약속 날짜와 작성된 약속의 개수를 표시해 줍니다.
- 만약 특정 날짜에 최근 새로 추가된 약속이 있다면, New 표시를 통해 사용자가 이를 알 수 있도록 합니다.



#### 날짜별 페이지

---

<img src="readme_Cr-Mo-Marco-3000.assets/image-20220609194138499.png" alt="image-20220609194138499" style="zoom:50%;" />

- 날짜를 클릭해서 들어갔을 때, 약속의 이름과 약속을 만든 사람, 약속 시간, 
  약속 장소와 현재 참여 인원 / 최대 참여 가능 인원이 표시되도록 합니다.



#### 약속 상세 페이지

---

<img src="readme_Cr-Mo-Marco-3000.assets/image-20220609201202010.png" alt="image-20220609201202010" style="zoom:50%;" />

- 약속에 대한 상세한 정보들과 어떤 약속인지에 대해 작성자가 작성한 내용이 표시됩니다.
- 서비스 이용자들은 참석 및 취소 버튼을 통해 약속 참석 여부를 결정할 수 있으며, 
  토글 버튼을 통해 약속 참여 인원들을 볼 수 있습니다. 
- 댓글 작성과 삭제도 가능하며, 토글 버튼을 통해  글에 달린 댓글들을 볼 수 있습니다.



### 부가 기능 소개



#### 마이페이지

---

<img src="readme_Cr-Mo-Marco-3000.assets/image-20220609214707371.png" alt="image-20220609214707371" style="zoom:50%;" />

- 마이페이지에서는 네 가지 항목을 볼 수 있습니다.
  - 오늘 예정된 약속은 오늘 아직 시간이 되지 않은 약속들을 모두 보여주고, 그 중 가장 가까운 약속 시간까지 남은 시간을 표시해 줍니다.
  - 내가 작성한 약속은 지금까지 내가 만들었던 약속을 모두 보여줍니다
  - 앞으로 예정된 약속에서는 약속 시간이 되지 않은 오늘의 약속들과 미래의 약속들을 보여줍니다. 
  - 내가 참석했던 약속은 약속 시간과 날짜가 지난 모든 약속들을 보여줍니다.
