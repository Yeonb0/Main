- [[JavaScript|JS]]로 [[DOM]] 조작하기


| 메서드                                        | 설명                  | 예시                                                |
| ------------------------------------------ | ------------------- | ------------------------------------------------- |
| `document.getElementById(id)`              | 특정 id의 요소 선택        | `document.getElementById('title')`                |
| `document.querySelector(selector)`         | CSS 선택자로 첫 번째 요소 선택 | `document.querySelector('.content')`              |
| `document.querySelectorAll(selector)`      | CSS 선택자로 모든 요소 선택   | `document.querySelectorAll('p')`                  |
| `element.textContent`                      | 요소의 텍스트 내용 변경/가져오기  | `element.textContent = '새로운 텍스트'`                 |
| `element.innerHTML`                        | 요소 내부 HTML 변경/가져오기  | `element.innerHTML = '<em>변경된 내용</em>'`           |
| `element.setAttribute(attr, value)`        | 요소의 속성 변경/추가        | `element.setAttribute('class', 'new-class')`      |
| `element.style.property`                   | CSS 스타일 직접 변경       | `element.style.color = 'red'`                     |
| `element.addEventListener(event, handler)` | 이벤트 등록              | `element.addEventListener('click', function(){})` |
| `document.createElement(tag)`              | 새 요소 생성             | `document.createElement('div')`                   |
| `element.appendChild(child)`               | 자식 요소 추가            | `parent.appendChild(newChild)`                    |