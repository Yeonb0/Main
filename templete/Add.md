<%*
// 링크 클릭 등 모든 방식으로 새 파일 생성 시 일일 노트에 링크 추가
const DAILY_FOLDER = "공부 기록";           // 일일 노트 폴더
const DAILY_FORMAT = "YYYY-MM-DD";      // 일일 노트 파일명 포맷

if (!window._dailyLinkHandlerRegistered) {
  window._dailyLinkHandlerRegistered = true;

  app.workspace.onLayoutReady(() => {
    app.vault.on("create", async (file) => {
      if (file.extension !== "md") return;

      const name = file.basename;
      const today = moment().format(DAILY_FORMAT);
      if (name === today) return;  // 일일 노트 자기 자신 스킵

      const daily = app.vault.getAbstractFileByPath(`${DAILY_FOLDER}/${today}.md`);
      if (!daily) return;

      // 이미 링크가 있으면 중복 추가 방지
      const content = await app.vault.read(daily);
      if (content.includes(`[[${name}]]`)) return;

      await app.vault.append(daily, `\n* [[${name}]] : `);
    });
  });
}
%>