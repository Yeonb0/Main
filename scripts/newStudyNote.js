module.exports = async (params) => {
  const { app, quickAddApi } = params;

  // 1. 노트 이름 물어보기 (한 번만)
  const noteName = await quickAddApi.inputPrompt("새 노트 이름:");
  if (!noteName) return;

  // 2. 새 노트 생성
  const newNotePath = `${noteName}.md`; // 폴더 지정하려면 "Folder/" + noteName + ".md"
  await app.vault.create(newNotePath, "");

  // 3. 오늘 daily note 경로 계산
  const dailyNoteName = window.moment().format("YYYY-MM-DD");
  const dailyNotePath = `Daily Notes/${dailyNoteName}.md`; // 실제 daily note 폴더명으로 수정

  // 4. daily note에 링크 append
  const dailyFile = app.vault.getAbstractFileByPath(dailyNotePath);
  if (dailyFile) {
    await app.vault.append(dailyFile, `\n- [[${noteName}]]`);
  }

  // 5. 새로 만든 노트 열기 (선택)
  const newFile = app.vault.getAbstractFileByPath(newNotePath);
  if (newFile) {
    await app.workspace.getLeaf().openFile(newFile);
  }
};